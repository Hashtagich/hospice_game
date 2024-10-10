import styles from './theHeader.module.css';


const TheHeader = () => {
    return (
        <header id='main' className={styles.header}>
            <div className={styles.container}>
                <div className={styles.wrapperLogo}></div>
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