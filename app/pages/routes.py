from flask import Blueprint, render_template
from .models import Project

blueprint = Blueprint('pages', __name__)

@blueprint.route('/projects')
def projects():
  all_projects = Project.query.all()
  return render_template('pages/index.html', project=all_projects)

@blueprint.route('/projects/<slug>')
def project(slug):
  project = Project.query.filter_by(slug=slug).first_or_404()
  return render_template('pages/projects-page.html', project=project)
