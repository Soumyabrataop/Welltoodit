from flask import Flask, request, jsonify, render_template, send_file, abort
from downloader import list_formats, download_video, sanitize_filename
import tempfile
import os

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/formats')
def api_formats():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400
    try:
        info = list_formats(url)
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/download')
def api_download():
    url = request.args.get('url')
    format_id = request.args.get('format_id')
    extract_audio = request.args.get('audio', 'false').lower() == 'true'
    if not url or not format_id:
        return jsonify({'error': 'Missing parameters'}), 400

    tmpdir = tempfile.mkdtemp(prefix='yt_dl_')
    try:
        out_path, filename = download_video(url, format_id, tmpdir, extract_audio=extract_audio)
        if not os.path.exists(out_path):
            return jsonify({'error': 'Download failed'}), 500
        # Stream the file as attachment
        return send_file(out_path, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # cleanup will be handled by the OS or left for manual cleanup for large files
        pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
