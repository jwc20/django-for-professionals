# Chapter 15: Search

## About

In this chapter we will learn how to implement basic search with forms and filters. Then we will improve it with additional logic and touch upon ways to go even more deeply with search options in Django. We only have three books in our database now but the code here will scale to as many books as we’d like.

## Instructions

- Update books app urls to include search endpoint.
  - Import SearchResultListView.
- Update books app views to connect to search_results template.
- Created search_results template in books app.
- Update books app views to filter a certain string.
- Update bokos app views to filter multiple strings. (225)

  - Import Q objects.

- Search Form:
  - Update book app base template to add search form in nav bar.
  - Update book app views to filter by input string from search form.
