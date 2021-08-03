import { useEffect, useState } from "react";
import ReactImage from 'react-image-wrapper'
import logo from './assets/theStar.png'



const NewsAPI = () => {

  const [news, setNews] = useState([]);
  const timeStamp = Intl.DateTimeFormat('en-US', {year: 'numeric', month: '2-digit',day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit'})

  useEffect(() => {
    fetch('http://localhost:8000/newsapi/api/lead/?format=json')
    .then(response=> response.json())
    .then(data => {
      setNews(data);
    }
     );
  }, [])

   
   

  
  return (  
    <div className="news-content">
       {
          news.map( (i) => (
           <div className="news-div" key={ i.id }>

             <div className="news-source-image" >
          
               <ReactImage 
                src={logo}
                width={70}
                height={70}
                shape="round"
                title="The Star"/>
             </div>

             <div className="news-headline">
               <h4>{ i.headline }</h4>
             </div>

             <div className="news-timestamp">
               <p>{ i.timestamp }</p>
             </div>
             
            </div>
            
            ))
       }
        
    </div>
  );
}
 
export default NewsAPI;

//  {/*
//           news.map( (i) => (
//                 <div className="news-headline" key={ i.id }>
//                   <Card>
//                   <Card.Body>{ i.headline }</Card.Body>
//                   </Card>
                  
                        
//                 </div>
//                 ))
//           */}


      //     <div className="news-source-image">
      //   <ReactImage 
      //   src="/"
      //   width={70}
      //   height={70}
      //   shape="round"
      //   title="The Star"/>
         
      
      // </div>
      // <div className="news-headline">
      //   <h2>News goes here</h2>
      // </div>
      // <div className="news-timestamp">
      //   <p>News timestamp</p>
      // </div>