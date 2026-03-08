from flask import Blueprint, render_template

#create blueprint object with prefixed name and url domain
death_slayers_bp = Blueprint('bp_death_slayers', __name__, url_prefix='/death_slayers')

# create route to tools page
@death_slayers_bp.route('/death_slayers_tools')
def death_slayers_tools():
    return render_template('death_slayers_tools.html')

@death_slayers_bp.route('/death_slayers_rules')
def death_slayers_rules():
    return render_template('death_slayers_rules.html')