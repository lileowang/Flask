import blog

if __name__ == "__main__":
    app = blog.create_app()
    app.run(debug=True)