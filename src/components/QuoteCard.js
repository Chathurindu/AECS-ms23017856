import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownAltIcon from '@mui/icons-material/ThumbDownAlt';

const QuoteCard = ({ username, text, likes, dislikes }) => {
  return (
    <Card variant="outlined" style={{ marginBottom: '10px' }}>
      <CardContent>
        <Typography variant="h5" component="div">
          {username}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {text}
        </Typography>
        <div>
        <IconButton color="primary" aria-label="add to shopping cart">
            <ThumbUpIcon />
        </IconButton>
          <span>{likes}</span>
          <IconButton style={{ marginLeft: '20px' }} color="error" aria-label="add to shopping cart">
            <ThumbDownAltIcon />
        </IconButton>
          <span> {dislikes}</span>
        </div>
      </CardContent>
    </Card>
  );
};

export default QuoteCard;
