from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)     #everytime code is changed it will rerun the server
