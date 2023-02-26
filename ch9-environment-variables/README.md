# Chapter 9: Environment Variables

## About

- Environment variables are variables that can be loaded into the operating environment of a project at run time as opposed to hard coded into the codebase itself.
- They allow a greater level of security and simpler local/production configurations.
- Environment variables make it much easier to switch between local and production code environments.

## Instructions

- Install environs.

```
docker-compose down
docker-compose up -d --build
```

- Update settings to use environs.
  - Import Env.
- Add django secret key to environment in docker-compose.yml.
- Update SECRET_KEY in settings to use key in docker-compose.yml. (144)

```
docker-compose down
docker-compose up -d
```

- Updated settings to use DJANGO_DEBUG in docker-compose.yml.
- Set DJANGO_DEBUG to true in docker-compose.yml environment variable.
- Updated DATABASE in settings to use the config in docker-compose.yml.

```
docker-compose down
docker-compose up -d
```
