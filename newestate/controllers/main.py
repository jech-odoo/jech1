from odoo import http
from odoo.http import request


class estateproperty(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World"

    @http.route('/hello_user', auth="user")
    def hello_user(self, **kw):
        return "Hello %s" % (request.env.user.name)

    @http.route('/hello_template', website=True)
    def hello_template(self, **kw):
        return request.render('newestate.hello_world')

    @http.route('/hello_template_user', website=True)
    def hello_template_user(self, **kw):
        properties = request.env['estate.properties'].search([])
        print("properties ::: ", properties)
        return request.render('newestate.hello_user', {'user': request.env.user, 'properties': properties})

    @http.route('/properties', website=True)
    def estate_properties(self, **kw):
        properties = request.env['estate.properties'].search([])
        return request.render('newestate.dynamic_template', {'user': request.env.user, 'properties': properties})
