from covid_full_stack_app.website import app  # noqa: F401

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
