
import { Link } from 'react-router-dom'


const Navbar = () => {
    
    

    return (  
       <div className="navbar">
           <Link to="/">Highlights</Link> 
           <Link to="/finance">Finance</Link> 
           <Link to="/politics">Politics</Link> 
           <Link to="/economy">Economy</Link> 
           <Link to="/technology">Technology</Link> 
           <Link to="/entertainment">Entertainment</Link> 
       </div>
    );
}
 
export default Navbar;