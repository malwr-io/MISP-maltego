from canari.maltego.entities import Hash, Domain, IPv4Address, URL, DNSName, AS, Website, NSRecord, PhoneNumber, EmailAddress, File, Location, Company, Alias, Port, Twitter
from MISP_maltego.transforms.common.entities import ThreatActor, Software, AttackTechnique

mapping_misp_to_maltego = {
    'AS': [AS],
    'domain': [Domain, NSRecord, Website, DNSName],
    'email-dst': [EmailAddress],
    'email-src': [EmailAddress],
    'filename': [File],
    'hostname': [Website, NSRecord, Domain, DNSName],
    'ip': [IPv4Address],
    'ip-dst': [IPv4Address],
    'ip-src': [IPv4Address],
    'md5': [Hash],
    'phone-number': [PhoneNumber],
    'sha1': [Hash],
    'sha224': [Hash],
    'sha256': [Hash],
    'sha384': [Hash],
    'sha512': [Hash],
    'sha512/224': [Hash],
    'sha512/256': [Hash],
    'ssdeep': [Hash],
    'impfuzzy': [Hash],
    'uri': [URL],
    'url': [URL],

    'whois-registrant-email': [EmailAddress],
    'country-of-residence': [Location],
    'github-organisation': [Company],
    'github-username': [Alias],
    'imphash': [Hash],
    'jabber-id': [Alias],
    'passport-country': [Location],
    'place-of-birth': [Location],
    'port': [Port],
    'target-email': [EmailAddress],
    'target-location': [Location],
    'target-org': [Company],
    'target-user': [Alias],
    'twitter-id': [Twitter],
    # object mappings
    'nameserver': [NSRecord],
    # custom types created internally for technical reasons
    # 'regkey_value': [Unknown]
}

mapping_galaxy_icon = {
    # "android": "malware",  # "android",
    "btc": "ransomware",
    "bug": "vulnerability",
    # "cart-arrow-down": "malware",  #"tds",
    "chain": "course_of_action",
    "door-open": "backdoor",
    "eye": "malware",
    "gavel": "tool",
    # "globe": "cert-eu-govsector",
    # "industry": "sector",
    # "internet-explorer": "exploit-kit",
    "key": "stealer",
    "map": "attack_pattern",
    "optin-monster": "malware",
    # "shield": "malpedia",
    # "shield": "preventive-measure",
    "sitemap": "botnet",
    "usd": "malware",  # "banker",
    # "user-secret": "mitre-intrusion-set",
    "user-secret": "threat_actor",
}

mapping_galaxy_type = {
    # 'amitt-misinformation-pattern': '',
    'android': Software,
    'backdoor': Software,
    'banker': Software,
    'botnet': Software,
    # 'branded-vulnerability': '',
    # 'cert-eu-govsector': '',
    'cloud-security': AttackTechnique,
    'exploit-kit': Software,
    'financial-fraud': AttackTechnique,
    'guidelines': AttackTechnique,
    'malpedia': Software,
    'microsoft-activity-group': ThreatActor,
    'mitre-attack-pattern': AttackTechnique,
    # 'mitre-course-of-action': '',
    'mitre-intrusion-set': ThreatActor,
    'mitre-malware': Software,
    'mitre-tool': Software,
    # 'preventive-measure': '',
    'ransomware': Software,
    'rat': Software,
    # 'region': '',
    # 'sector': '',
    'social-dark-patterns': AttackTechnique,
    'stealer': Software,
    'surveillance-vendor': ThreatActor,
    # 'target-information': '',
    'tds': Software,
    'threat-actor': ThreatActor,
    'tool': Software
}

mapping_object_icon = {
    'ail-leak': '',
    'ais-info': '',
    'android-permission': '',
    'annotation': '',
    'anonymisation': 'AffiliationAnonymous',
    'asn': '',
    'attack-pattern': '',
    'authenticode-signerinfo': '',
    'av-signature': '',
    'bank-account': '',
    'bgp-hijack': '',
    'blog': 'URL',
    'btc-transaction': 'BankCard',
    'btc-wallet': 'BankAccount',
    'cap-alert': '',
    'cap-info': '',
    'cap-resource': '',
    'coin-address': 'BankAccount',
    'command': '',
    'command-line': '',
    'cookie': 'Cookies',
    'cortex': '',
    'cortex-taxonomy': '',
    'course-of-action': 'course_of_action',
    'covid19-csse-daily-report': '',
    'covid19-dxy-live-city': '',
    'covid19-dxy-live-province': '',
    'cowrie': '',
    'credential': '',
    'credit-card': 'BankCard',
    'crypto-material': 'Encrypt',
    'cytomic_orion': '',
    'cytomic_orion_machine': '',
    'dark-pattern': '',
    'ddos': '',
    'device': '',
    'diameter-attack': '',
    'dns-record': 'ServerDNS',
    'domain-crawled': '',
    'domain-ip': 'NetworkGlobal',
    'elf': '',
    'elf-section': '',
    'email': 'Email',
    'employee': 'Person',
    'exploit-poc': 'Person',
    'facial-composite': '',
    'fail2ban': '',
    'file': 'File',
    'forensic-case': '',
    'forensic-evidence': '',
    'forged-document': '',
    'geolocation': 'GPS',
    'gtp-attack': '',
    'http-request': 'URL',
    'ilr-impact': '',
    'ilr-notification-incident': '',
    'impersonation': 'GangBoss',
    'imsi-catcher': 'MobileNet',
    'instant-message': 'Form',
    'instant-message-group': '',
    'intelmq_event': '',
    'intelmq_report': '',
    'internal-reference': '',
    'interpol-notice': '',
    'iot-device': 'InternetISP',
    'iot-firmware': '',
    'ip-api-address': '',
    'ip-port': 'NetworkCard',
    'irc': '',
    'ja3': '',
    'leaked-document': 'InternetDocument',
    'legal-entity': 'Company',
    'lnk': 'File',
    'macho': '',
    'macho-section': '',
    'mactime-timeline-analysis': '',
    'malware-config': 'Virus',
    'meme-image': '',
    'microblog': '',
    'mutex': '',
    'netflow': '',
    'network-connection': 'NetworkSymmetric',
    'network-socket': '',
    'news-agency': '',
    'news-media': '',
    'organization': 'Company',
    'original-imported-file': 'File',
    'passive-dns': 'ServerDNS',
    'paste': 'InternetDocument',
    'pcap-metadata': '',
    'pe': 'File',
    'person': 'Person',
    'pe-section': '',
    'pgp-meta': '',
    'phishing': 'InternetDocument',
    'phishing-kit': '',
    'phone': 'PhoneNumber',
    'process': '',
    'python-etvx-event-log': '',
    'r2graphity': '',
    'regexp': '',
    'registry-key': 'RegistryErase',
    'regripper-NTUser': '',
    'regripper-sam-hive-single-user': '',
    'regripper-sam-hive-user-group': '',
    'regripper-software-hive-appInit-DLLS': '',
    'regripper-software-hive-application-paths': '',
    'regripper-software-hive-applications-installed': '',
    'regripper-software-hive-BHO': '',
    'regripper-software-hive-command-shell': '',
    'regripper-software-hive-general-windows-info': '',
    'regripper-software-hive-software-run': '',
    'regripper-software-hive-userprofile-winlogon': '',
    'regripper-system-hive-firewall-configuration': '',
    'regripper-system-hive-general-configuration': '',
    'regripper-system-hive-network-information': '',
    'regripper-system-hive-service-drivers': '',
    'report': 'Resume',
    'research-scanner': '',
    'rogue-dns': '',
    'rtir': '',
    'sandbox-report': 'Resume',
    'sb-signature': '',
    'scrippsco2-c13-daily': '',
    'scrippsco2-c13-monthly': '',
    'scrippsco2-co2-daily': '',
    'scrippsco2-co2-monthly': '',
    'scrippsco2-o18-daily': '',
    'scrippsco2-o18-monthly': '',
    'script': '',
    'shell-commands': '',
    'shodan-report': '',
    'shortened-link': 'URL',
    'short-message-service': '',
    'splunk': '',
    'ss7-attack': '',
    'ssh-authorized-keys': '',
    'stix2-pattern': '',
    'suricata': '',
    'target-system': 'sighting',
    'threatgrid-report': '',
    'timecode': '',
    'timesketch_message': '',
    'timesketch-timeline': '',
    'timestamp': '',
    'tor-hiddenservice': '',
    'tor-node': '',
    'tracking-id': '',
    'transaction': '',
    'translation': '',
    'trustar_report': '',
    'TSK-Chats': '',
    'TSK-Web-Bookmark': '',
    'TSK-Web-Cookie': '',
    'TSK-Web-Downloads': '',
    'TSK-Web-History': '',
    'TSK-Web-Search-Query': '',
    'url': 'URL',
    'user-account': 'User',
    'vehicle': 'Car',
    'victim': 'Victim',
    'virustotal-graph': '',
    'virustotal-report': '',
    'vulnerability': 'vulnerability',
    'weakness': 'vulnerability',
    'whois': 'VINNumber',
    'x509': 'MedicalRecord',
    'yabin': '',
    'yara': '',
}

# All possible default icons shipped with Maltego - useful for auto_completion
# AccessCard
# AccessPoint
# Accident
# Accountant
# Add
# Admin
# AdultFemale
# AdultMale
# AffiliationAndroid
# AffiliationAnonymous
# AffiliationApple
# AffiliationBebo
# AffiliationBlogger
# AffiliationBuiltWith
# AffiliationCloud
# AffiliationColdfusion
# AffiliationDigg
# AffiliationDropbox
# AffiliationEbay
# AffiliationFacebook
# AffiliationFlickr
# AffiliationGoogleDrive
# AffiliationGooglePlus
# AffiliationInstagram
# AffiliationKik
# AffiliationLinkedIn
# AffiliationLinux
# AffiliationMeetup
# AffiliationMyspace
# AffiliationNewsvine
# AffiliationOrkut
# AffiliationPayPal
# AffiliationPicasa
# AffiliationPinterest
# Affiliation
# AffiliationReddit
# AffiliationRSS
# AffiliationSkype
# AffiliationSnapchat
# AffiliationSpock
# AffiliationTinder
# AffiliationTwitter
# AffiliationWechat
# AffiliationWhatsapp
# AffiliationWiki
# AffiliationWindows
# AffiliationWWF
# AffiliationYammer
# AffiliationYelp
# AffiliationYouTube
# AffiliationZoomInfo
# AircraftBomber
# AircraftCarrier
# AirCrash
# Airport
# Alarm
# Alias
# Alliance
# Ammunition
# Anarchy
# Antenna
# Apartments
# Army
# Artist
# Assemble
# Asteroid
# Atom
# Author
# Baby
# Backbone
# Ballerina
# BandAid
# BankAccount
# BankCard
# Banner
# Bear
# Bee
# Binary
# BioAgent
# Bit
# BlueAura
# Bomb
# BookPDF
# Book
# BorderCheckpoint
# Businessman
# BusinessPhoneSystem
# Bus
# CableUSB
# Camera
# Captive
# Cargo
# Car
# CashInTransit
# Cash
# CellNetwork
# Cemetery
# CEO
# Certificate
# Certification
# Champion
# CheckBox
# Checkpoint
# ChemicalAnalysis
# Child
# Church
# CircularArea
# City
# Clock
# ClusterOrange
# Cluster
# CoffeeShop
# ColoredBall
# Community
# Company
# ConferenceAudio
# Connect
# Contract
# ControlTower
# Cookies
# CrimeScene
# Criminal
# CV
# Dam
# DatabaseConnect
# DatabaseErase
# Database
# DateField
# Deceased
# Degree
# Delete
# Desert
# Desktop
# Destroy
# Diamond
# Diary
# Dictator
# Directions
# Disabled
# Disconnect
# DNACode
# Donation
# Donkey
# Drone
# DrugDealer
# Earthquake
# Elderly
# Elephant
# Email
# Encrypt
# Environment
# Erase
# Event
# Explosion
# Factory
# Farm
# FastFood
# Fax
# FieldDelete
# Field
# File
# FileSharing
# Files
# Filter
# FingerPrint
# FireForest
# Firewall
# Fix
# FlightNumber
# FlightPath
# Flood
# FloppyDisk
# Form
# GamingConsole
# GangBoss
# GangMember
# Gang
# GasStation
# Gateway
# Genealogy
# Genetic
# Geography
# GhostSighting
# GlobalWarming
# Gorilla
# GovermentOfficial
# Government
# GPS
# Green2Grey
# Green2Orange2Turquoise
# Green2Red2Blue
# Group
# Guard
# Gun
# Hacker
# Harbour
# HardDisk
# Harvest
# Hashtag
# Headphones
# Helicopter
# Home
# HospitalLocation
# Hostage
# Hotel
# Hurricane
# HydroPower
# IconManager
# ID
# IED
# ImageField
# Image
# Influencer
# InfoMessage
# InternetDocument
# InternetFastSpeed
# InternetIP
# InternetISP
# InternetMIMEDocs
# InternetMIMEFolder
# InternetMIME
# Internet
# InternetUser
# Invasion
# ISBN
# Island
# Judge
# KeyPrimary
# Keys
# KillerWhale
# Knife
# Last
# LawEnforcementOfficer
# Lawyer
# Leader
# License
# LinkBroke
# Link
# List
# Lobby
# Location
# Log
# MacAddress
# MaltegoGraph
# ManyIn
# Marijuana
# MedicalRecord
# Medicine
# MeetingBusiness
# MeetingSocial
# Memorial
# MergeCells
# Messenger
# MilitaryOfficer
# Mine
# MissileRPG
# MissingPerson
# MobileComputer
# MobileNet
# MobilePhone
# MobileUser
# Modem
# Monitoring
# Moon
# Mosque
# Motorbike
# Movie
# Murder
# MusicAlbum
# MusicSinger
# MusicSongwriter
# MXRecord
# MySQL
# Neighborhood
# NetAdmin
# NetworkAdmin
# NetworkAsymetric
# NetworkCardBlue
# NetworkCard
# NetworkConnector
# NetworkDistribution
# NetworkGlobal
# NetworkHub
# NetworkID
# NetworkIntranet
# NetworkISDN
# NetworkMonitor
# NetworkSoftware
# NetworkSymmetric
# News
# Node
# NSRecord
# NuclearPlant
# Nurse
# Objects
# OilField
# OilSpill
# OilWell
# OnlineGroup
# Orange2Green
# Orange2Purple
# Organization
# OSIModel
# Passport
# PasswordPHP
# Password
# Patient
# Person
# PetrolBomb
# PhoneConversation
# PhoneLandlineOffice
# PhoneLandlineResidential
# PhoneNumber
# Phrase
# Pilot
# Piracy
# Pirate
# Plane
# Planet
# Play
# Poison
# PoliticalParty
# Port
# PowerPlant
# Prescription
# PrisonCamp
# Prisoner
# Prison
# Privilege
# ProgressBar
# Protester
# Protest
# Protocol
# Purple2Turquoise
# PurplePink2Green
# PurplePink2Yellow2Blue
# QRCode
# Quarantine
# QuestionDialog
# Radar
# Radio
# Rain
# Red2Blue
# Red2Green
# Red2Yellow
# RefugeeCamp
# RegistrationPlate
# RegistryErase
# RelationshipModel
# Relationship
# RemoteControl
# Repeater
# Reporter
# Restaurant
# Resume
# Rhino
# Rocket
# Role
# Route
# Router
# Royalty
# RunningWater
# Satellite
# Savings
# School
# Science
# Scientist
# Script
# SecurityCameraMonitoring
# SecurityCheckpoints
# Security
# Seed
# Sentiment
# ServerBackup
# ServerChat
# ServerDNS
# ServerFTP
# ServerMicrosoftSQL
# Server
# ServerProxy
# Service
# SexOffender
# Sharing
# SharkAttack
# ShipContainer
# ShipCruise
# ShipPirate
# Ship
# ShipSpeed
# ShipTanker
# ShipTrawler
# ShipYacht
# Shop
# SIMCard
# SiteFTP
# SizeAllLinks
# SizeInLinks
# SizeOutLinks
# SmileConfused
# SmileMad
# Smile
# SmileSad
# SMS
# Sniffer
# Snow
# Socket
# SoftwareBlocking
# SoftwareCollaborative
# SoftwareFTP
# SoftwareManager
# SoftwareMeeting
# Software
# Soldier
# Solidarity
# Space
# SpaceStation
# Spider
# SplitCells
# Spy
# Spyware
# SQLQuery
# SSLCertificate
# SSL
# SSN
# Star
# Stop
# SuicideBomber
# SUNET
# Suspect
# SuspiciousPerson
# Switch
# Sybase
# SynagogueTemple
# Syndicate
# Table
# TabletTouch
# Tag
# Tank
# TargetPerson
# Target
# Taxi
# Technician
# Temple
# Terminal
# TerroristLeader
# TerroristMember
# TerroristThug
# Terror
# TextField
# Theatre
# Ticket
# TradeUnion
# Train
# TrainStation
# Transform
# Trojan
# Truck
# TsetseFly
# Tsunami
# Turquoise2Orange2Red
# Turquoise2Yellow
# TV
# UFOAbduction
# Underground
# Universe
# UnknownBody
# Unknown
# UPS
# Urgent
# URL
# USB
# UserID
# User
# Victim
# VideoCamera
# Videoconference
# VINNumber
# Virus
# Voice
# VOIP
# VolcanoEruption
# VPN
# WAN
# WebDir
# Website
# WiFi
# WindFarm
# WirelessRouter
