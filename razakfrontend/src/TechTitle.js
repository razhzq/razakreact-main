import ReactImage from 'react-image-wrapper'
import tech from './assets/techicon.svg'



const TechTitle = () => {
    return ( 
        <div className="tech-title">
            <h3>Technology</h3>
            <div className="tech-image">
              <ReactImage 
                src={tech}
                width={30}
                height={30}
                title="Technology"
           />
            </div>
        </div>
     );
}
 
export default TechTitle;