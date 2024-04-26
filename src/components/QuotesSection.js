import React from 'react';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

function QuotesSection({ quotes }) {
  return (
    <Box mt={4}>
      <Typography variant="h6" gutterBottom>
        Quotes
      </Typography>
      {quotes.map((quote, index) => (
        <Typography key={index} variant="body1" gutterBottom>
          {quote}
        </Typography>
      ))}
    </Box>
  );
}

export default QuotesSection;
