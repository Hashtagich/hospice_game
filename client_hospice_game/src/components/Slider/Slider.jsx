import { useState } from 'react';
import { sliderData } from '../../datas/dataSlider';
import styles from './slider.module.css';


export default function Slider() {

    const [indexSlider, setIndexSlider] = useState(0);

    const arrowLeft = () => {
        if(indexSlider <= 0) {
            setIndexSlider(sliderData.length - 1);
        }else {
            setIndexSlider(prev => prev - 1);
        }
            
    };

    const arrowRight = () => {
        if(indexSlider >= 2) {
            setIndexSlider(0);
        }else {
            setIndexSlider(prev => prev + 1);
        }
    };

    return (
        <div>
            {sliderData.map((item, itemIndex) => {

                return (
                    <div className={indexSlider === itemIndex ? styles.positionActive : styles.positionSlide} key={item.id}>
                        <img className={styles.image} src={item.image} alt={'game foto'}/>
                    </div>
                )
    })}
            <div className={styles.containerDots}>
                <div onClick={arrowLeft} className={styles.arrowLeft}></div>
                {Array.from({length: 3}).map((item, index) => {

                    return (
                        <div key={index} onClick={() => setIndexSlider(index)}
                        className={indexSlider === index ? styles.activeDote : styles.dot}>
                    </div>
                    )
                })}
                <div onClick={arrowRight} className={styles.arrowRight}></div>
            </div>
        </div>
    )
};

