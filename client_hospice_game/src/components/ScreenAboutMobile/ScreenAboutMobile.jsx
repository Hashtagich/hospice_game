import styles from './screenAboutMobile.module.css';
import Button from '../Button/Button';
import imagePhone from '../../images/phone.png';
import imagePhoneMobile from '../../images/phoneForMobile.png'



const ScreenAboutMobile = () => {
    return (
        <section id='mobilegame' className={styles.container}>
            <img src={imagePhone} className={styles.image} alt="Foto mobile phone"></img>
            <div className={styles.wrapperDescriptionMobileVersion}>
                <h1 className={styles.sectionName}>Мобильная версия</h1>
                <p className={styles.description}>Можно играть и на мобильном устройстве</p>
                <img src={imagePhoneMobile} className={styles.imageMobile} alt="Foto mobile phone"></img>
                <a className={styles.bottomLine} href='https://www.google.com/search?sca_esv=825e01edc18a56f7&sca_upv=1&sxsrf=ADLYWIKI52P7Uu0rnVoklJJOY581fToAlQ:1726587935177&q=Minecraft&stick=H4sIAAAAAAAAAEWSy2sTURTGM8WGZFqhSVEkuKjVRegm856MCK1oBcEi1C5045B5JnPvPO9lXisR3BcX_gGuXLhQiiBVS3Eh2IVEQVGEIi4EEemygqImbeZmFgO_e8_5vvOdmcrkPN1yW4wSSyCwuZP9p_2Nt7f6j-b6L4av5_2t_uPB2bP-Zv_JDnW0ZbdY1nJTDCyQF9zNPR1ItkOYdUVoWzJhWcR64MCCdZiJCtD4HerAGiiarjAj4CQNsfYIDocaQZQhwIBCw2FCXkQuKtgw1DiP3faoOE-gbZMBbRt5KgYuYQ0wuSJEpDnVQBaFPHHCDh-QYguAhJPROC0vwahdONkYw2gw1tQQWMZqI6wXpZouyjhDUnHLCgbm0x2qMiTZhgrxMCTZy1OSTnccEQJLJRtPNSkFhkWEc8TlKhoHUDm-LalELzKU1OUkYZyhm6hQ10gGxla7SsIUHBiREnka0Y-kKGK0QBxlRHYXI1JsBQzvGAlZiBOoGjLgIPX04TCZw2IlJN6SaAtBlBRL4FzOkqSRchwASctIbMSwIOXwDlU9-Be6QBnvMuEEAQI8ahRDIfQ44oE8RkFqd7yfmE1ZIyH3HM_YTBwXjBgnjJEGxzMmsQdAWjA2BA8BRP5gS9ZChUXwK7VPTc18_7U72_hJ3X34-gP1jaJnrvg-MmG2asIONo01v36cLi97uIez-nSDpg--tsiAdn2Znrpm4jV_xTd6VlaX6gJdXTFdzYzQVat-mqYv-BCaOu75Xv1YY5autXRy0LI7ronOTjSp-ZC7ufnu3pvy9Vpp8Hxsri41mgs1unzRdzs9r1Z69Wf3_KUfiwuzdGWtk_qe72a1y3t__535vbc4f6o66PmycePT4rB76c7nc9snqLkjzRI7FNt_L28vlNYnqNtbD16WKxVqpsRNVEp5afr-ZHWl55l61LHwepn6DzMDCqo4BAAA&sa=X&stq=1&lei=NKTpZpHOFYeC1fIPl_mL6Q8' rel="noopener noreferrer" target='_blank'><Button className={styles.button} nameButton='Перейти'/></a>
                <Button className={styles.buttondisable} nameButton='Перейти'/>
                <h3 className={styles.infoDisabledButton}>Доступно на мобильном</h3>
            </div>
        </section>
    )
};

export default ScreenAboutMobile;