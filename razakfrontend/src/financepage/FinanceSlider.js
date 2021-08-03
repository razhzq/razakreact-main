
import Slider from 'react-animated-slider';
import 'react-animated-slider/build/horizontal.css';



const FinanceSlider = () => {

    const slides = [
        {title:'First News Headline', description: 'Lorem Ipsum'},
        {title:'Second News Headline',description:'Lorem Ipsum'}
    ]
    

    return ( 
        <div className="finance-slider">
        <Slider>
        {slides.map((slide, index) => 
          <div className="finance-slider-text" key={index}>
             <h2>{slide.title}</h2>
             <div>{slide.description}</div>
         </div>)}
        </Slider>
     </div>
     );
}
 
export default FinanceSlider;