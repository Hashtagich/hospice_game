import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import { sliderDataMobile } from '../../datas/dataSlider';
import 'swiper/css/pagination';
import './stylesMobile.css';


const Swiperslider = () => {
    return (
        <Swiper
        initialSlide="1"
        slidesPerView={1}
        centeredSlides={true}
        spaceBetween={30}
        grabCursor={true}
        className="mySwiper"
        >
            {sliderDataMobile.map((slide) => (
                <SwiperSlide key={slide.id}><img src={slide.image} alt='slides'></img></SwiperSlide>
            ))}
        </Swiper>
    )
};

export default Swiperslider;