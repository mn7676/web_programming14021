import { Link } from "react-router-dom";
import './Header.module.css'

const Header = () => {
    return (
    <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/game">Game</Link>
          </li>
        </ul>
      </nav>
    );
  };
  
  export default Header;