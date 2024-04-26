import React, { useState } from 'react';
import { Amplify } from 'aws-amplify';
import { awsExports } from './aws-exports';
import { Authenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import ResponsiveAppBar from './components/ResponsiveAppBar';
import ProfessionInput from './components/ProfessionInput'; // Import the ProfessionInput component
import Container from '@mui/material/Container';

Amplify.configure(awsExports);

function App() {
  const [user, setUser] = useState(null);

  const handleStateChange = (authState, authData) => {
    setUser(authData);
  };

  return (
    <Authenticator onStateChange={handleStateChange}>
      {({ signOut, user }) => (
        <div>
          <ResponsiveAppBar signOut={signOut} />
          <div>
            {user && (
              <div>
                <Container>
                <h1 className="text-3xl font-bold underline">Welcome {user.username}</h1>
                <ProfessionInput username={user.username} />
                </Container>
              </div>
            )}
          </div>
        </div>
      )}
    </Authenticator>
  );
}

export default App;
