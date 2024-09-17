import styles from './app.module.css';
import ScreenMain from '../src/components/ScreenMain/ScreenMain';
import ScreenAboutGame from '../src/components/ScreenAboutGame/ScreenAboutGame';
import ScreenAboutRealCenter from '../src/components/ScreenAboutRealCenter/ScreenAboutRealCenter';
import ScreenAboutHero from '../src/components/ScreenAboutHero/ScreenAboutHero';
import ScreenAboutGameplay from '../src/components/ScreenAboutGameplay/ScreenAboutGameplay';
import ScreenAboutMobile from '../src/components/ScreenAboutMobile/ScreenAboutMobile';
import Button from './components/Button/Button';

function App() {
	return (
		<>
			<main>
				<ScreenMain/>
				<ScreenAboutGame/>
				<ScreenAboutRealCenter/>
				<ScreenAboutHero/>
				<ScreenAboutGameplay/>
				<ScreenAboutMobile/>
			</main>
			<footer className={styles.footer}>
				<a href='https://detireb.ru/' target='_blank'><Button className={styles.button} nameButton='ПОМОЧЬ'/></a>
				<div className={styles.wrapperLinksIcons}>
					<a href='https://ok.ru/' target='_blank'><div className={styles.odnoklassniki}></div></a>
					<a href='https://web.telegram.org/k/' target='_blank'><div className={styles.telega}></div></a>
					<a href='https://vk.com/' target='_blank'><div className={styles.vk}></div></a>
				</div>
				<h3 className={styles.textFooter}>© 2024 Company</h3>
			</footer>
		</>
	);
}

export default App;
