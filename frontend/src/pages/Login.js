import React, { useState } from 'react';
import Signup from '../components/Signup/Signup';
import Signin from '../components/Signin/Signin';

const Login = () => {
  const [isSignin, setIsSignin] = useState(true)

  return (
    <div>
      <button onClick={()=>setIsSignin(!isSignin)}>
      {isSignin? "switch to signup" : "switch to signin" }
      </button>
      {isSignin? <Signin /> : <Signup /> }
    </div>
  );
};

export default Login;