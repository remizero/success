# Create the project entrypoint (wsgi.py).

The wsgi.py file is the entry point for every Success project. While there are other ways to run a Flask project, it is the industry standard and who is Success to change that?

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Create wsgi.py file](#create-wsgipy-file)
* [Content of the wsgi.py file](#content-of-the-wsgipy-file)
* [Template](#template)
* [Next step](#next-step)

---

## Create wsgi.py file

If you have not yet created the `wsgi.py` file, a quick way to do it is:

  ```bash
    touch wsgi.py
  ```

---

## Content of the wsgi.py file 🧩

After creating the `wsgi.py` file, copy the following code to define our entrypoint for our Success project:

  ```bash
    cat <<EOF >> wsgi.py
    # Python Libraries / Librerías Python

    # Success Libraries / Librerías Success
    from success.Success import Success

    # Preconditions / Precondiciones
    success = Success ()
    success.create ()
    app = success.getApp ()


    if __name__ == "__main__" :
      success.run ()
    EOF
  ```

---

## Template. (recommended) ⚡

The fastest way to get started is by copying the `wsgi.py` template included in the examples directory.

  ```bash
    cp examples/wsgi.py <path/my_project/wsgi.py>
  ```

---

## Next step. 🔗

[APPLICATIONS.md](APPLICATIONS.md)
