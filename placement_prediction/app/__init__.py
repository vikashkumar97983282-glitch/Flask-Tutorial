from flask import Flask



def create_app():

    app = Flask(__name__)

    from app.routes import home_bp
    from app.routes import about_bp
    from app.routes import predict_bp
    from app.routes import content_bp
    from app.routes import developer_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(content_bp)
    app.register_blueprint(developer_bp)

    return app