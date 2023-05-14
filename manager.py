import os
import warnings

from flask import send_from_directory
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flaskr import create_app
from flaskr.extensions import db

warnings.filterwarnings("ignore")
app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 设置icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == "__main__":
    manager.run()
