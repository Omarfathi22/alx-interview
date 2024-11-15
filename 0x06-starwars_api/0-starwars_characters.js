#!/usr/bin/node

// Import the 'request' module to perform HTTP requests
const request = require('request');

// Get the movie ID from the command line argument (second argument)
const movieId = process.argv[2];

// Define the API endpoint to fetch film data using the movieId
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;

// Initialize an empty array for character URLs and an array for storing character names
let people = [];
const names = [];

// Function to request character URLs from the film API endpoint
const requestCharacters = async () => {
    // Make an asynchronous HTTP request to fetch film data
    await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
        if (err || res.statusCode !== 200) {
            // Log any errors or unsuccessful HTTP status codes (non-200)
            console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
            // If the request is successful, parse the JSON response body
            const jsonBody = JSON.parse(body);
            // Store the character URLs in the 'people' array
            people = jsonBody.characters;
            resolve();
        }
    }));
};

// Function to request character names based on the character URLs
const requestNames = async () => {
    // Check if the 'people' array has any character URLs
    if (people.length > 0) {
        // Loop through each character URL
        for (const p of people) {
            // Make an asynchronous HTTP request to fetch character data
            await new Promise(resolve => request(p, (err, res, body) => {
                if (err || res.statusCode !== 200) {
                    // Log any errors or unsuccessful HTTP status codes (non-200)
                    console.error('Error: ', err, '| StatusCode: ', res.statusCode);
                } else {
                    // If the request is successful, parse the JSON response body
                    const jsonBody = JSON.parse(body);
                    // Push the character name into the 'names' array
                    names.push(jsonBody.name);
                    resolve();
                }
            }));
        }
    } else {
        // If no character URLs were found, log an error
        console.error('Error: Got no Characters for some reason');
    }
};

// Main function to get character names and print them
const getCharNames = async () => {
    // Call requestCharacters to fetch character URLs from the movie
    await requestCharacters();

    // Call requestNames to fetch the names of the characters from their URLs
    await requestNames();

    // Print the character names to the console
    for (const n of names) {
        // If it's the last name in the array, print it without a newline
        if (n === names[names.length - 1]) {
            process.stdout.write(n);
        } else {
            // Otherwise, print each name followed by a newline
            process.stdout.write(n + '\n');
        }
    }
};

// Invoke the getCharNames function to fetch and print the character names
getCharNames();
