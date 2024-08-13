from fasthtml.common import *
from css import mcss
#from js import openSide, closeSide
from js import myjavascript


fav = Favicon('#', '#')

# Javascript 
myjava = Script(myjavascript)
# CSS 
css = Style(mcss)

app,rt = fast_app(live=True, pico=False, hdrs=(fav, css, myjava), ws_hdr=True)

# Our navigation sidebar
SideBar = Div(A('<', id="closebtn", href='javascript:void(0)', cls='closebtn', onclick='closeSide()'),
            A('Home', hx_get='/', hx_target="#content", hx_swap="outerHTML"),  
            A('About', hx_get='/about', hx_target="#content", hx_swap="outerHTML"),
            A('Services', hx_get='/services', hx_target="#content", hx_swap="outerHTML"),
            A('Clients', hx_get='/clients', hx_target="#content", hx_swap="outerHTML"),
            A('Contact', hx_get='/contact', hx_target="#content", hx_swap="outerHTML"),
            id='sideBar', cls='sidebar')


def home_page():
    """ Content that will be displayed when the user refreshes the page or via the menu using an htmx get"""
    return Div(P("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ips", id="interesting"), P("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ips", id="interesting"), id="content")


@rt('/')
def get(request):
	# We will check the headers and if it is a htmx request only send the 'content', otherwise the full page
    client_headers = request.headers
    # Only send the content
    if 'hx-request' in client_headers:
        return home_page()
    else:
    # Send the full page
        return SideBar, Div(Button('>', cls='openbtn', onclick='openSide()', id='openbtn'),
                        Div(home_page(), id="homepage"),
                        id='main')

@rt('/about')
def get():
    return Div(P("About", id="interesting"), id="content")

@rt('/services')
def get():
    return Div(P("Services", id="interesting"), id="content")

@rt('/clients')
def get():
    return Div(P("Clients", id="interesting"), id="content")

@rt('/contact')
def get():
    return Div(P("Contact", id="interesting"), id="content")

serve()
