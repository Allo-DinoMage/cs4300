Feature: Movie Theater Booking
  As a user
  I want to view movies and book seats
  So that I can watch movies at the theater

  Scenario: View movie listings
    Given the database has movies
    When I visit the movies page
    Then I should see a list of movies

  Scenario: View available seats
    Given the database has movies
    And the database has seats
    When I visit the seat booking page for a movie
    Then I should see available seats

  Scenario: View empty booking history
    Given I am a logged in user
    When I visit the booking history page
    Then I should see an empty booking history

  Scenario: API returns movies
    When I request the movies API
    Then the response status should be 200

  Scenario: API returns seats
    When I request the seats API
    Then the response status should be 200

  Scenario: Unauthenticated user cannot access bookings API
    When I request the bookings API without authentication
    Then the response status should be 403
