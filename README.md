
<div align="center">
    <img src="project_images/Project_logo.jpg" width="12%">
    <br>
    <h3 align="center">⚡National Grid weekly</h3>
    <p>Create a weekly summary of energy passsing <br> through Great Britain's national grid</p>
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

## About this project
<p align="center">
    <img src="images/2026-08-10_2026-08-16.png" alt="treemap" width="50%"/>
</p>

Where does get its Great Britain's energy? 

Behind the electricity we consume in our homes and businesses sits a vast network of generators and interconnectors. This project aims to demistify where our energy is coming from in a simple, stylish treemap visualization.

While many brilliant projects that summarise the National Grid's energy network already exist, this script creates elegant visualizations explicitly designed for social media - the idea being we should share data with people in the places they already spend their time.

### Built with
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
* ![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=ffffff)
* ![NumPy](https://img.shields.io/badge/numpy-4D77CF?style=for-the-badge&logo=numpy&logoColor=ffffff)
* ![Jupyter](https://img.shields.io/badge/jupyter-EB7325?style=for-the-badge&logo=jupyter&logoColor=ffffff)

## Getting started
### Prerequisites
The `requirements.txt` file lists all the Python libraries necessary for you to run this script. To install them all run:

```
pip install -r requirements.txt
```

### Installation


## Usage


## Roadmap
- [ ] Add automated posting to Instagram w/ instagrapi
- [ ] Improve labelling for smaller treemap slices
- [ ] Allow custom date ranges for plot data

## Data sources
**Elexon - Generation by fuel type** 
<br>
The Elexon generation by fuel type API reports electricity generation across Great Britain. Values are returned as average megawatts over a 30 minute period known as a 'Settlement period'. 

There are 48 settlement periods in a 24 hour period, with the exception of days when clocks change.

[Link](https://bmrs.elexon.co.uk/generation-by-fuel-type)

**NESO - Demand update**
<br>
Most of Great Britain's solar power is embedded, meaning it is not connected directly to the National Grid's long range transmission networks. 

This excludes solar from the Elexon outrun data used above, so we use NESO's demand CSV to include solar in our final visualization.

[Link](https://bmrs.elexon.co.uk/generation-by-fuel-type)

## Acknowledgements
Thank you to Kate Morley who's fantastic [National Grid: Live](https://grid.iamkate.com/) was both the inspiration for this project and an invaluable resource for getting it to work properly.
