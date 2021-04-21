package main

import (
	"log"

	argparser "github.com/alexflint/go-arg"
)

var args struct {
	Register *RegisterArgs `arg:"subcommand:register"`
	Login    *LoginArgs    `arg:"subcommand:login"`
	Host     string        `default:"127.0.0.1"`
	Port     string        `default:"3000"`
}

func main() {
	argparser.MustParse(&args)

	switch {
	case args.Register != nil:
		registerUser()
	case args.Login != nil:
		userSignIn()
	default:
		log.Fatal("Unrecognized command.")
	}

}
