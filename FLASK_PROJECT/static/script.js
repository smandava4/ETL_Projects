document.addEventListener('DOMContentLoaded', function() {
  // Fetch user information
  fetch('/user_info')
    .then(response => response.json())
    .then(data => {
      const userInfoDiv = document.getElementById('user-info');
      userInfoDiv.innerHTML = `
        <p><strong>Name:</strong> ${data.name}</p>
        <p><strong>Description:</strong> ${data.description}</p>
        <!-- Add more user information here -->
      `;
    })
    .catch(error => {
      console.error('Error fetching user info:', error);
    });

  // Handle tweet submission
  document.getElementById('tweet-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const tweetText = document.getElementById('tweet-text').value;
    fetch('/post_tweet', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ tweet_text: tweetText })
    })
      .then(response => response.json()) // Parse the response as JSON
      .then(data => {
        // Display the response message including tweet ID on the page
        const responseDiv = document.getElementById('tweet-response');
        responseDiv.textContent = `Tweet ID: ${data.tweet_id} - ${data.message}`;
      })
      .catch(error => {
        console.error('Error posting tweet:', error);
      });
  });

  // Handle tweet deletion
  document.getElementById('delete-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const tweetId = document.getElementById('tweet-id').value;
    fetch(`/delete_tweet/${tweetId}`, {
      method: 'DELETE'
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to delete tweet');
        }
        console.log('Tweet deleted successfully');
        // Refresh user information after deleting tweet
        location.reload();
      })
      .catch(error => {
        console.error('Error deleting tweet:', error);
      });
  });
});
