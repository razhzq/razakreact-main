import { Carousel } from 'react-responsive-carousel';
import ReactImage from 'react-image-wrapper'


const TopNews = () => {
    
    
    
    return (  
       <div className="top-news">
          <div className="image">
           <ReactImage 
             src="#"
             width={400}
             height={350}
           />
          </div>
         <div className="top-article">
            <h1>The Global IPO Market Has Never Been Than It Is Right Now</h1>
            <p>News Description</p>
         </div>
       </div>
       
    );
}
 
export default TopNews;