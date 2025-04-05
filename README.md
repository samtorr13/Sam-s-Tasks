# Sam's Task App
![Static Badge](https://img.shields.io/badge/Descargar-Github-green?logo=github&link=https%3A%2F%2Fgithub.com%2Fsamtorr13%2FSam-s-Tasks%2Freleases%2Ftag%2Fv0.0.2-Alpha)(https://github.com/samtorr13/Sam-s-Tasks/releases)

Una app de tareas simple escrita en flet, por los momentos aún se encuentra en desarrollo, por lo que no es 100% estable.

trataré de actualizar todas las noches, espero lograrlo

## Run the app
### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).
