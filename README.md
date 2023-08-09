# nyx-art

A few definitions before we start:


**Individuation**: process to achieve a sense of individuality that separates the individual from others.<br/>
**Generative art**: a process of algorithmically generating new ideas, forms, shapes, colors or patterns, based on a set of rules that provide boundaries for the creation process. In the NFT (web3) world, it means that the artist provide a set of traits (images) and an algorithm randomizes these traits and creates one-of-one art (no 2 final art pieces are the same).<br/>
**Soul**: As participants of the experiment did their individuation, they received an NFT ERC-721 token called “Soul”, with their personality traits represented on the token art.<br/>
**Ferrymen**: generative art (NFT ERC-721) token given to Soul holders who participated on the experiment.<br/>


## Introduction

As part of the NYX experiment, 2 NFT ERC-721 tokens were created:
- Soul NFT: art derived from the individuation traits of each holder
- Ferrymen NFT: generative art

This repository contains the code and summary for the generative art of Souls and Ferrymen. Other repositories for this project: <br/>
Machine Learning: https://github.com/tpancier/nyx-ml <br/>
node.js: https://github.com/tennydesign/nyx
<br/><br/>
Jupyter notebooks in this repository:<br/>
Souls generation: XXXX<br/>
Ferryment generation: XXX
<br/><br/>
Project webpage: https://nyxsoul.webflow.io/

For more information about the research behind this project: [nyxxp medium](https://nyxxp.medium.com/this-is-a-research-on-possible-ways-to-digitize-the-human-soul-using-jungian-theory-psychometrics-ead7f7ad4632)https://nyxxp.medium.com/this-is-a-research-on-possible-ways-to-digitize-the-human-soul-using-jungian-theory-psychometrics-ead7f7ad4632

## Architecture

<img width="638" alt="NYX architecture" src="https://github.com/community/community/assets/19897750/e517650b-c347-4ebb-8a87-683543618b56">


## Souls creation

The process for Souls was:
- Mint a Soul NFT (website + Ethereum Smart Contract)
- Complete your individuation (Discord with custom bots)
- Soul NFT was then revealed on OpenSea, the art based on their individuation traits and put together based on python algorithm. The chance of two Souls being the same is 1 in 7,194,667,451,811,840,000.

The code created by this project and used to generate the Souls art is innovative. It requires less than 5 minutes for the Soul art to be revealed, involving several systems (Discord, SQL database, virtual server/droplet in Digital Ocean). Normally NFTs are revealed in batches and may take a few days.


Example of trait:

<img width="286" alt="Soul trait" src="https://github.com/community/community/assets/19897750/c279738b-eae6-47d7-9c5b-9bfb23a2028c">


Example of final art (tokens in OpenSea):

<img width="1058" alt="souls final art" src="https://github.com/community/community/assets/19897750/2d7aee95-5d9b-4c93-90c2-0ecf14ad54b1">

OpenSea collection: https://opensea.io/collection/nyx-ai?search[stringTraits][0][name]=State&search[stringTraits][0][values][0]=Soulbind

## Ferrymen creation


Ferrymen art was created with a generative art algorithm, randomizing almost 300 trait images, broken into 2 characters (Tempest and Oblivion) and more than 10 groups (background, hair, hat, clothing, skin among others). The logic for this part of the project is unique. Due to the complexity of the art, the traits exception handling had to be coded and offer an interface to be easily customized.

Example of trait:

<img width="638" alt="cloth trait 2" src="https://github.com/community/community/assets/19897750/96729588-23cd-4a2f-b16d-28de9f6ab5ce">


Example of final art (tokens in OpenSea):

<img width="1061" alt="ferrymen final art" src="https://github.com/community/community/assets/19897750/7de7dedd-4eaf-46b8-85fa-7fc0d9b79d27">


OpenSea collection: https://opensea.io/collection/the-ferrymen


