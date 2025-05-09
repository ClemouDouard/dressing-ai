<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">Dressing AI</h1>

  <p align="center">
    A streamlit application that uses a pre-trained model to recommend outfits based on the user's input.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The goal is to be able to select the perfect outfit fast. We will use computer vision to classify the different clothes, use a `SQL` database to store the data. And then, we will use a LLM to find the perfect outfit for the day.
Everything would be in a streamlit application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![SQLite][SQLite]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

  ```sh
  python3.12 -m venv venv
  source venv/bin/activate
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ClemouDouard/dressing-ai.git
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Work in progress

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Structure of the project
- [x] Authentification system
  - [x] Users table
  - [x] Add it to the setup_db.py script
  - [x] Add a user
  - [x] Make a login page
- [ ] Image management
  - [ ] Make an upload button
  - [ ] Extract features from the image
  - [ ] Print those features on the page to make sure that the user is happy with the result
  - [ ] Save the image and its features in the database
- [ ] Recommendation system
- [ ] Deployment

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/ClemouDouard/ebooks_generator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ClemouDouard/ebooks_generator" alt="contrib.rocks image" />
</a>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ClemouDouard/ebooks_generator](https://github.com/ClemouDouard/ebooks_generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[contributors-url]: https://github.com/ClemouDouard/ebooks_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[forks-url]: https://github.com/ClemouDouard/ebooks_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[stars-url]: https://github.com/ClemouDouard/ebooks_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[issues-url]: https://github.com/ClemouDouard/ebooks_generator/issues
[license-shield]: https://img.shields.io/github/license/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[license-url]: https://github.com/ClemouDouard/ebooks_generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/clementleveque
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Streamlit-url]: https://streamlit.io/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
[CrewAI-url]: https://www.crewai.com/
[CrewAI]: https://img.shields.io/badge/CrewAI-000000?style=for-the-badge&logo=CrewAI&logoColor=white
[Mistral-url]: https://mistral.ai/
[Mistral]: https://img.shields.io/badge/Mistral-000000?style=for-the-badge&logo=Mistral&logoColor=white
[Python-url]: https://www.python.org/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Matplotlib-url]: https://matplotlib.org/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=Matplotlib&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Pandas]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white
[Plotly-url]: https://plotly.com/
[Plotly]: https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=Plotly&logoColor=white
[Seaborn-url]: https://seaborn.pydata.org/
[Seaborn]: https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=Seaborn&logoColor=white
[SQLite-url]: https://www.sqlite.org/
[SQLite]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white