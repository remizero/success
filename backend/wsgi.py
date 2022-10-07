from kernel import Success

app = Success.create ()
#wsgi_app = app.wsgi_app ()

if __name__ == "__main__" :
  app.run (host='0.0.0.0')