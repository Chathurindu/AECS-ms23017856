import React, { useState, useEffect } from 'react';
import MediaCard from './MediaCard'; 
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import QuoteCard from './QuoteCard';

const ProfessionInput = ({ username }) => {
  const [profession, setProfession] = useState('');
  const [userExists, setUserExists] = useState(false);
  const [profileCreated, setProfileCreated] = useState(false);
  const [quote, setQuote] = useState('');
  const [quotes, setQuotes] = useState([]);

  const handleGetQuotes = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/get_quotes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' // Set the content type to application/json
        },
        body: JSON.stringify({
          username: username
        })
      });
      const data = await response.json();
      if (data.quotes) {
        setQuotes(data.quotes);
      } else {
        console.error('Error retrieving quotes:', data.error);
      }
    } catch (error) {
      console.error('Error retrieving quotes:', error);
    }
  };

  // Refresh the quotes every 2 seconds
  useEffect(() => {
    const intervalId = setInterval(handleGetQuotes, 2000);

    // Clear interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  useEffect(() => {
    // Function to check if the username exists
    const checkUsername = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/check_username/${username}`);
        const data = await response.json();
        setUserExists(data.msg !== "Item not found!");
      } catch (error) {
        console.error('Error checking username:', error);
      }
    };

    // Only call the checkUsername function if username is not empty
    if (username) {
      checkUsername();
    }
  }, [username]);

  const handleAddUserProfile = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/add_user_profile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          profession: profession
        })
      });
      const data = await response.json();
      console.log('Response from adding user profile:', data);
      if (data.message === 'Profile created successfully') {
        setProfileCreated(true); // Set profileCreated state to true after profile creation
      } else {
        console.error('Error creating user profile:', data.error);
      }
    } catch (error) {
      console.error('Error adding user profile:', error);
    }
  };

  const handleGenerateQuote = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5001/inspirational_quote');
      const data = await response.json();
      if (data.quote) {
        setQuote(data.quote);
        // Add the quote to the user's profile
        await addQuoteToProfile(data.quote);
      } else {
        console.error('Error fetching quote:', data.error);
      }
    } catch (error) {
      console.error('Error fetching quote:', error);
    }
  };

  const addQuoteToProfile = async (quote) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/add_quote', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          quote: quote
        })
      });
      const data = await response.json();
      console.log('Response from adding quote to profile:', data);
    } catch (error) {
      console.error('Error adding quote to profile:', error);
    }
  };


  return (
    <div>
      {!userExists && !profileCreated && (
        <div>
          <input type="text" value={profession} onChange={(e) => setProfession(e.target.value)} placeholder="Enter profession" />
          <button onClick={handleAddUserProfile}>Add Profile</button>
        </div>
      )}
      <div>
      <Box sx={{ p: 2 }}>
      <Button variant="contained" onClick={handleGenerateQuote}>Generate Quote</Button>
      </Box>
      {/* <MediaCard username={username} profession={profession} /> */}
      </div>
      {/* {quote && <p>{quote}</p>} */}
      <div>
        {quotes.map((quote) => (
          <QuoteCard
            key={quote.quote_id}
            username={quote.username}
            text={quote.quote_text}
            likes={quote.likes}
            dislikes={quote.dislikes}
          />
        ))}
      </div>
    </div>
  );
}

export default ProfessionInput;
