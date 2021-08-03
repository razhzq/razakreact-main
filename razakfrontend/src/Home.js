import Line from './LineDivide'
import Finance from './FinanceTitle'
import MainSlider from './MainSlider';
import FinanceHighlight from './FinanceHighlight';
import TechTitle from './TechTitle';
import TechHighlight from './TechHighlight';




const Home = () => {
    return (  
        <div className="home">
            <MainSlider />
            <Line />
            <Finance />
            <FinanceHighlight />
            <Line />
            <TechTitle />
            <TechHighlight />
        </div>
    );
}
 
export default Home;