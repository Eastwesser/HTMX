# Flask x HTMX
Use `hx-get`, `hx-post`, `hx-put`, `hx-patch`, and `hx-delete` commands instead of typing in JavaScript.

To run the application try:

  ```
  flask run
  ```

Stage 1:
- Flask application initialization

Stage 2:
- HTMX installation

Stage 3:
- Ping 
  - on click 
  - on ctrl + click
  - on shift + click
- Hover
- HTMX
  - `ht-swap="outerHTML"` 
  - `hx-trigger="mouseenter"`
  - `ht-trigger="click[shiftKey]"`

Stage 4:
- Clicker via HTMX

Stage 5:
- Embed clicker into index page via HTMX

Stage 6:
- Handle HTMX boosts

Stage 7:
- Handle products CRUD list

Stage 8:
- Handle & create CRUD list, loading via HTMX
- Added creation a new element and return only the new rendered element via ```hx-swap="beforeend"```
- Processing using 'out of band' (hs-swap-oob)
- Handle form error 422
- Return many html files for replacement: form and oob-item

Stage 9:
- What-The-Forms (Flask)
- Added CSRF protection from Flask WTF
- Processing CSRF form Flask WTF for adding the new product

Stage 10:
- Added HTMX (CSRFToken) Headers
- CSRF exempt example in 'rest/examples/views.py'

Stage 11:
- Products CRUD: Handle delete HTMX animation
- Main DELETE function (after icon click)
- Delete product by ID, closest tag choice: `hx-target="closest li"`
- Delete product by ID, via product-item class choice: `hx-target="closest .product-item"`
- Animations: loading `.htmx-request` and swapping `.htmx-swapping`

Stage 12:
- Product update:
  - PUT query,
  - Error processing (form)

Stage 13:
- HTMX Push url - browser history replacement
- `hx-target="body"`
- `hx-confirm`

Stage 14:
- Products CRUD: HTMX Reveal load + paginate
- Auto-Loading in an infinite list (with Animation)
- `hx-trigger="revealed"`

Stage 15:
- Products CRUD: HTMX regular pagination with buttons

# This REST API is still under development, check links for more info:

## URLs
- https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/
- https://htmx.org/essays/hateoas/#:~:text=Hypermedia%20as%20the%20Engine%20of,provide%20information%20dynamically%20through%20hypermedia.
- https://steveklabnik.com/writing/nobody-understands-rest-or-http
- https://steveklabnik.com/writing/some-people-understand-rest-and-http

### HTTP
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

### HTMX
- https://htmx.org/
- https://htmx.org/docs/
- https://htmx.org/examples/animations/
- https://htmx.org/attributes/hx-trigger/
- https://htmx.org/attributes/hx-target/
- https://htmx.org/attributes/hx-boost/
- https://htmx.org/attributes/hx-post/
- https://htmx.org/attributes/hx-swap-oob/
- https://htmx.org/attributes/hx-swap/
- https://htmx.org/attributes/hx-headers/
- https://htmx.org/attributes/hx-indicator/
- https://htmx.org/attributes/hx-request/
- https://htmx.org/attributes/hx-push-url/
- https://htmx.org/attributes/hx-confirm/

### Flask
- https://flask.palletsprojects.com/en/3.0.x/
- https://jinja.palletsprojects.com/en/3.1.x/templates/
- https://flask-wtf.readthedocs.io/en/1.2.x/
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/#javascript-requests
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/#exclude-views-from-protection

### Static
- https://freesvg.org/trash-can-icon
- https://www.svgbackgrounds.com/elements/animated-svg-preloaders/
