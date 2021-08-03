
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NewsAPI from './NewsAPI';
import Header from './Header';
import Navbar from './Navbar'
import Home from './Home'
import Finance from './financepage/Finance'


function App() {
  return (
    <Router>
      <div className="App">
         <Header />
         <Navbar />
       <div className="content">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/finance">
            <Finance />
          </Route>
          
        </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
