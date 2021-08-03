import ReactImage from 'react-image-wrapper'
import finance from './assets/financeicon.png'



const Finance = () => {
    
    
    
    
    return (
        <div className="finance-title">
            <h3>Finance</h3>
            <div className="finance-image">
              <ReactImage 
                src={finance}
                width={30}
                height={30}
                title="Finance"
           />
            </div>
        </div>
      );
}
 
export default Finance;