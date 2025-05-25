/*
    This JavaScript file provides the functionality for handling user interactions
    within the stock market prediction application. It includes the following features:
    1. Displaying the selected company's name when the dropdown selection changes.
    2. Handling the form submission, preventing page reload, and sending data to the server using an AJAX request.
    3. Displaying the predicted closing price for the selected stock based on the response.
    4. Handling errors and displaying appropriate error messages.
*/

// Wait for the document to be fully loaded
$(document).ready(function () {

    // Event listener for when the company dropdown changes
    $("#company").change(function () {
        // Get the selected company name
        const selectedCompany = $(this).find("option:selected").text();

        // If a company is selected (i.e., it's not the placeholder)
        if (selectedCompany !== "Select a company") {
            // Display the selected company name in the designated div
            $("#selectedCompany").text(`Selected Company: ${selectedCompany}`);
        } else {
            // If no company is selected, clear the selected company text
            $("#selectedCompany").text('');
        }
    });

    // Event listener for form submission
    $("#predictionForm").submit(function (event) {
        event.preventDefault(); // Prevent the form from refreshing the page

        // Send the form data to the server using an AJAX POST request
        $.ajax({
            type: "POST", // Specify the HTTP method
            url: "/predict", // URL to send the request to
            data: $(this).serialize(), // Serialize the form data to send
            success: function (response) {
                // If the request was successful
                if (response.success) {
                    // Display the predicted closing price in the result section
                    $("#predictionResult").html(
                        `<h2>${response.company} Stock Price Prediction</h2>
                         <p><strong>Predicted Close Price:</strong> $${response.predicted_close.toFixed(2)}</p>`
                    );
                } else {
                    // If there was an error with the prediction, display the error message
                    $("#predictionResult").html(
                        `<p style="color: red;"><strong>Error:</strong> ${response.error}</p>`
                    );
                }
            },
            error: function () {
                // If the request failed (e.g., due to network issues), show a generic error message
                $("#predictionResult").html(
                    `<p style="color: red;"><strong>Error:</strong> Could not reach the server. Please try again later.</p>`
                );
            }
        });

        // Clear only the form inputs, but keep the selected company visible
        $("#predictionForm")[0].reset();
    });
});
