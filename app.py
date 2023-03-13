from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
app.config.from_object('config')

projects_data = {
  'project1' : 'cream design',
  'project2' : 'ebay kleinanzeigen',
  'project3' : 'design research'
}

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about-me')
def about_me():
  return render_template('about-me.html')

@app.route('/projects')
def projects():
  return render_template('projects.html', project = projects_data)

@app.route('/projects/<placeholder>')
def project(placeholder):

  if placeholder in projects_data:
    return render_template('projects-page.html', project_name = projects_data[placeholder])
  else:
    return render_template('projects-page.html', project_name = "the project does not exist")
if __name__ == '__main__':
  app.run()

# add the rountes for the other pages as well and make them how you did them with the home page and connect them with the links #