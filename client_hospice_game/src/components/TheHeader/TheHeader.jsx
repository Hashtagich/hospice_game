import styles from './theHeader.module.css';
import Burgermenu from '../Burgermenu/Burgermenu';
import Button from '../Button/Button';
import { useState } from 'react';


const TheHeader = () => {

const [isOpen, setIsOpen] = useState(false)

const openBurger = () => setIsOpen(prev => !prev)

const closeBurger = () => setIsOpen(false);

    return (
        <header id='main' className={styles.header}>
            <div className={styles.container}>
                <div className={styles.wrapperLogo}></div>
                <nav className={!isOpen ? styles.navburger : styles.cross}>
                    <Button click={openBurger} className={styles.buttonBurger}></Button>
                    {isOpen && <Burgermenu closeBurger={closeBurger}/>}
                </nav>
                <nav className={styles.nav}>
                    <ul className={styles.wrapperNavigation}>
                        <li className={styles.li}><a className={styles.linkAncor} href='#aboutgame'>Об игре</a></li>
                        <li className={styles.li}><a className={styles.linkAncor} href='#featuresgame'>Особенности</a></li>
                        <li className={styles.li}><a className={styles.linkAncor} href='#gameplay'>Геймплей</a></li>
                        <li className={styles.li}><a className={styles.linkAncor} href='#mobilegame'>Мобильная версия</a></li>
                        <li className={styles.li}><a className={styles.linkAncor} href='#realcenter'>РЦ "Мозайка"</a></li>
                    </ul>
                </nav>
            </div>
        </header>
    )
};

export default TheHeader;