/**
 * Author: Damodar Lohani
 * profile: https://github.com/lohanidamodar
 */

import 'package:flutter/material.dart';
import 'package:flutter_swiper_null_safety/flutter_swiper_null_safety.dart';

import 'login_view.dart';
import 'login_view.dart';

class OnboardingView extends StatefulWidget {
  @override
  _OnboardingViewState createState() => _OnboardingViewState();
}

class _OnboardingViewState extends State<OnboardingView> {
  SwiperController _controller = SwiperController();
  int _currentIndex = 0;
  final List<String> titles = [
    "Welcome",
    "Awesome App",
    "Flutter App",
    "Flutter Appt",
    "Flutter Appt",
  ];
  final List<String> subtitles = [
    "Welcome to this awesome intro screen app.",
    "This is an awesome app, of intro screen design",
    "Flutter is awesome for app development",
    "Flutter is awesome for app developmentb",
    "Flutter is awesome for app developmentb",
  ];
  final List<Color> colors = [
    Colors.green.shade300,
    Colors.blue.shade300,
    Colors.indigo.shade300,
    Colors.orange.shade300,
    Colors.lime.shade300,
  ];

  final List<Image> images = [
    Image.asset('assets/images/01.jpg'),
    Image.asset('assets/images/02.jpg'),
    Image.asset('assets/images/03.jpg'),
    Image.asset('assets/images/04.jpg'),
    Image.asset('assets/images/05.jpg'),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: <Widget>[
          Swiper(
            loop: false,
            index: _currentIndex,
            onIndexChanged: (index) {
              setState(() {
                _currentIndex = index;
              });
            },
            controller: _controller,
            pagination: const SwiperPagination(
              builder: DotSwiperPaginationBuilder(
                activeColor: Colors.teal,
                activeSize: 20.0,
              ),
            ),
            itemCount: colors.length,
            itemBuilder: (context, index) {
              return IntroItem(
                title: titles[index],
                subtitle: subtitles[index],
                bg: colors[index],
                imagePath: images[index],
              );
            },
          ),
          Align(
            alignment: Alignment.bottomLeft,
            child: MaterialButton(
              child: const Text("Skip"),
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (context) => LoginPage()),
                );
              },
            ),
          ),
          Align(
            alignment: Alignment.bottomRight,
            child: IconButton(
              icon: Icon(_currentIndex == colors.length - 1
                  ? Icons.check
                  : Icons.arrow_forward),
              onPressed: () {
                if (_currentIndex != colors.length - 1) {
                  _controller.next();
                } else {
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (context) => const LoginPage()),
                  );
                }
              },
            ),
          )
        ],
      ),
    );
  }
}

class IntroItem extends StatelessWidget {
  final String title;
  final String? subtitle;
  final Color? bg;
  final Image? imagePath;

  const IntroItem(
      {Key? key, required this.title, this.subtitle, this.bg, this.imagePath})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: bg ?? Theme.of(context).primaryColor,
      child: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: <Widget>[
              const SizedBox(height: 40),
              Text(
                title,
                style: const TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 35.0,
                    color: Colors.white),
              ),
              if (subtitle != null) ...[
                const SizedBox(height: 20.0),
                Text(
                  subtitle!,
                  style: const TextStyle(color: Colors.white, fontSize: 24.0),
                  textAlign: TextAlign.center,
                ),
              ],
              const SizedBox(height: 40.0),
              Expanded(
                child: Container(
                  margin: const EdgeInsets.only(bottom: 70),
                  width: double.infinity,
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(30.0),
                    child: Material(
                      color: Colors.white,
                      child: imagePath,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
