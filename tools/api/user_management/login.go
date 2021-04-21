package main

import "log"

type LoginArgs struct {
	Username string `arg:"required"`
	Password string `arg:"required"`
}

func userSignIn() {
	log.Fatal("Not yet implemented.")
}
