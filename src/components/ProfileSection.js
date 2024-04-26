import React from 'react';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

function ProfileSection({ user }) {
  return (
    <Box display="flex" alignItems="center">
      <Avatar sx={{ width: 100, height: 100, mr: 2 }} />
      <Box>
        <Typography variant="h5" gutterBottom>
          {user.username}
        </Typography>
        <Typography variant="subtitle1" gutterBottom>
          Profession: {user.profession}
        </Typography>
        <Typography variant="subtitle1" gutterBottom>
          Followers: {user.followers}
        </Typography>
      </Box>
    </Box>
  );
}

export default ProfileSection;
