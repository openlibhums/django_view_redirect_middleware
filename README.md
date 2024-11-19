# Django View Redirect Middleware

A Django middleware that redirects requests based on the current view name for non-staff users.

## Installation

## Install a Specific Release

To install a specific release, replace `<tag>` with the desired version tag (e.g., `v1.0`):

```bash
pip install -e git+ssh://git@github.com/openlibhums/django_view_redirect_middleware.git@<tag>#egg=django_view_redirect_middleware

```

## Clone and Install Locally

Alternatively, you can clone the repository and install it locally:

1. Clone the repository:
   ```bash
   git clone git@github.com:openlibhums/django_view_redirect_middleware.git
   ```

2. Navigate to the directory:
   ```bash
   cd django_view_redirect_middleware
   ```

3. Install the package:
   ```bash
   pip install .
   ```

## Usage

1. Add `'django_view_redirect_middleware.middleware.ViewRedirectMiddleware'` to your `MIDDLEWARE` in `settings.py`:

    ```python
    MIDDLEWARE = [
        # Other middleware...
        'django_view_redirect_middleware.middleware.ViewRedirectMiddleware',
    ]
    ```

2. Define `REDIRECT_VIEWS` and `REDIRECT_URL_NAME` in your `settings.py`:

    ```python
    REDIRECT_VIEWS = [
        'view_name_1',
        'view_name_2',
    ]

    REDIRECT_URL_NAME = 'redirect_url_name'
    ```

- `REDIRECT_VIEWS`: A list of view names that should trigger a redirect.
- `REDIRECT_URL_NAME`: The name of the URL to redirect to.


## License

GNU Affero General Public License v3