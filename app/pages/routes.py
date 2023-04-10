from flask import Blueprint, render_template, request, current_app
from .models import Project

blueprint = Blueprint('pages', __name__)

@blueprint.route('/projects')
def projects():
  page_number = request.args.get('page', 1, type=int)
  projects_pagination = Project.query.paginate(page_number, current_app.config['PROJECTS_PER_PAGE'])
  return render_template('pages/index.html', projects_pagination=projects_pagination)

@blueprint.route('/projects/<slug>')
def project(slug):
  project = Project.query.filter_by(slug=slug).first_or_404()
  return render_template('pages/projects-page.html', project=project)
