import os.path

from flask import Flask, current_app, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from xml.etree.ElementTree import parse, ParseError
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = '7f8766ce00d3b12b'


class UploadForm(FlaskForm):
    upload_file = FileField(validators=[FileAllowed(['xml'])])


@app.get('/')
def index():
    upload_form = UploadForm()
    return render_template('index.html', form=upload_form)


@app.post('/iatidoc')
def post_doc():
    save_dir = os.path.join(current_app.root_path, 'static/files')
    temp_dir = os.path.join(current_app.root_path, 'static/temp')
    upload_form = UploadForm()
    if upload_form.validate_on_submit():
        file = upload_form.upload_file.data
        # save file to temp dir
        temp_file_path = os.path.join(temp_dir, file.filename)
        file.save(temp_file_path)
        try:
            tree = parse(temp_file_path)
            root_tag = tree.getroot().tag
            if root_tag == 'iati-activities':
                random_hex = secrets.token_hex(8)
                _, file_ext = os.path.splitext(file.filename)
                new_filename = random_hex + file_ext
                file_path = os.path.join(save_dir, new_filename)
                file.save(file_path)
                os.remove(temp_file_path)
                flash(f'{new_filename} has been uploaded', 'success')
                return redirect(url_for('index'))
            flash('Invalid file', 'danger')
            return redirect(url_for('index'))
        except ParseError:
            # Invalid xml file
            flash('Invalid document', 'danger')
            return redirect(url_for('index'))

    flash('Invalid document', 'danger')
    return redirect(url_for('index'))
