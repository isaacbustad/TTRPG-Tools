from flask import Blueprint, render_template

pathfinder2e_pages_bp = Blueprint("bp_pathfinder2e", __name__, url_prefix='/pathfinder2e')

@pathfinder2e_pages_bp.route('/pathfinder2e_tools')
def pathfinder2e_tools():
    return render_template('pathfinder2e_tools.html')